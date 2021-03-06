# Generated by Django 2.1.1 on 2018-10-09 12:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='购买数量')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsModel', verbose_name='商品')),
            ],
            options={
                'verbose_name': '订单商品关系',
                'verbose_name_plural': '订单商品关系',
                'db_table': 'order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 10, 9, 20, 39, 2, 140415), verbose_name='创建时间')),
                ('is_pay', models.BooleanField(verbose_name='是否支付')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='总价')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel', verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单管理',
                'verbose_name_plural': '订单管理',
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='ordergoodsmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderModel', verbose_name='订单'),
        ),
    ]
