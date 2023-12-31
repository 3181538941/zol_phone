# Generated by Django 4.1 on 2023-05-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0004_phone_spu"),
    ]

    operations = [
        migrations.AddField(
            model_name="phone_spu",
            name="camera_back",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="后置摄像头"
            ),
        ),
        migrations.AddField(
            model_name="phone_spu",
            name="camera_front",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="前置摄像头"
            ),
        ),
        migrations.AddField(
            model_name="phone_spu",
            name="cpu",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="cpu"
            ),
        ),
        migrations.AddField(
            model_name="phone_spu",
            name="display_resolution",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="分辨率"
            ),
        ),
        migrations.AddField(
            model_name="phone_spu",
            name="ram",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ram"
            ),
        ),
        migrations.AddField(
            model_name="phone_spu",
            name="screen_size",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="屏幕尺寸"
            ),
        ),
    ]
