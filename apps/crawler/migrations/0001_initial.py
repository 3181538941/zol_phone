# Generated by Django 4.1 on 2023-05-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone_brand",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="品牌名称",
                    ),
                ),
                ("img_url", models.CharField(max_length=255, verbose_name="品牌图片")),
                (
                    "img_url_s3",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to="",
                        verbose_name="品牌图片local",
                    ),
                ),
                (
                    "market_share",
                    models.FloatField(
                        blank=True, max_length=255, null=True, verbose_name="市场占有率"
                    ),
                ),
                ("feedback", models.CharField(max_length=255, verbose_name="好评率")),
                ("price_min", models.CharField(max_length=255, verbose_name="最低价")),
                ("price_max", models.CharField(max_length=255, verbose_name="最高价")),
                ("phone_num", models.CharField(max_length=255, verbose_name="机型数量")),
            ],
            options={
                "verbose_name": "手机品牌",
                "verbose_name_plural": "手机品牌",
                "db_table": "phone_brand",
            },
        ),
        migrations.CreateModel(
            name="Phone_sku",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=124,
                        primary_key=True,
                        serialize=False,
                        verbose_name="手机id",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="手机名称/型号")),
                (
                    "intro",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="手机简介"
                    ),
                ),
                (
                    "price",
                    models.IntegerField(blank=True, null=True, verbose_name="手机价格"),
                ),
                (
                    "score",
                    models.FloatField(blank=True, null=True, verbose_name="手机评分"),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="手机详情页url"
                    ),
                ),
                (
                    "img_url",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="手机图片"
                    ),
                ),
                (
                    "comments_num",
                    models.IntegerField(blank=True, null=True, verbose_name="手机评论数"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="此条信息创建时间"),
                ),
            ],
            options={
                "verbose_name": "手机基本信息",
                "verbose_name_plural": "手机基本信息",
                "db_table": "phone_sku",
            },
        ),
        migrations.CreateModel(
            name="Spider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("run_times", models.IntegerField(default=0)),
                ("last_run_time", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "爬虫",
                "verbose_name_plural": "爬虫",
                "db_table": "spider",
            },
        ),
    ]
