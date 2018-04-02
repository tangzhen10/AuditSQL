# Generated by Django 2.0.2 on 2018-03-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0006_auto_20180329_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataexport',
            name='status',
            field=models.CharField(choices=[('0', '未生成'), ('1', '执行中'), ('2', '已生成')], default='0', max_length=2, verbose_name='生成进度'),
        ),
    ]