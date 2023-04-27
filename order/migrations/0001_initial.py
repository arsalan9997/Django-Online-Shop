# Generated by Django 4.2 on 2023-04-25 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
        ('basket', '0002_alter_basket_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('shipping_price', models.SmallIntegerField(default=0)),
                ('status', models.CharField(choices=[('PE', 'PENDING'), ('DO', 'DONE')], default='PE', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shipping.address')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='basket.basket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
