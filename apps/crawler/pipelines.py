# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from django.db import IntegrityError

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import md5sum
from loguru import logger
from hashlib import md5

from utils.minio.minio_s3 import MinioS3, get_public_url
from apps.crawler import settings


# from apps.crawler.models import Brand


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item
        # try:
        #     product = Brand(**item)
        #     product.save()
        # except IntegrityError:
        #     raise DropItem("Duplicate item found: %s" % item['name'])
        # return item


class MyImagePipeline(ImagesPipeline, ):
    def get_media_requests(self, item, info):
        """
        重写get_media_requests方法, 用于下载图片, 生成一个request,
        当一个单独项目中的所有图片请求完成时，该方法会被调用。
        处理结果会以二元组的方式返回给 item_completed() 函数。这个二元组定义如下：(success, image_info_or_failure: dict)
        其中，第一个元素表示图片是否下载成功；第二个元素是一个字典，包含三个属性：
        1) url - 图片下载的url。这是从 get_media_requests() 方法返回请求的url。
        2) path - 图片存储的路径（类似 IMAGES_STORE）
        3) checksum - 图片内容的 MD5 hash
        """
        img_url = item.get("img_url")
        yield Request(img_url, meta={'item': item})

    # @logger.catch()
    def file_path(self, request, response=None, info=None, *, item=None):
        """
        重写file_path方法, 用于自定义图片存储路径及文件名
        """
        _file_name = request.meta['item']['name']
        name_md5 = md5()  # 使用MD5加密模式
        name_md5.update(_file_name.encode('utf-8'))  # 将参数字符串传入
        name_md5 = name_md5.hexdigest()  # 获取加密串
        md5_file_name = f"{name_md5}.{request.url.split('.')[-1]}"
        print(f"{md5_file_name=}")
        return md5_file_name

    def item_completed(self, results, item, info):
        images = [x for ok, x in results if ok]
        # print(f"{images=}")
        return item

    @logger.catch
    def image_downloaded(self, response, request, info, *, item=None):
        checksum = None
        for path, image, buf in self.get_images(response, request, info, item=item):
            if checksum is None:
                buf.seek(0)
                checksum = md5sum(buf)
            width, height = image.size
            self.store.persist_file(
                path,
                buf,
                info,
                meta={"width": width, "height": height},
                headers={"Content-Type": "image/jpeg"},
            )
            item["img_local"] = get_public_url(path)
        return checksum
