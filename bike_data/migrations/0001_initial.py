# Generated by Django 4.2.7 on 2023-11-14 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField(unique=True, verbose_name='대여소 번호')),
                ('station_name', models.CharField(max_length=200, verbose_name='대여소명')),
                ('location', models.CharField(max_length=200, verbose_name='자치구')),
                ('addr1', models.CharField(max_length=200, verbose_name='주소1')),
                ('addr2', models.CharField(max_length=200, null=True, verbose_name='주소2')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='위도')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=11, verbose_name='경도')),
            ],
        ),
        migrations.CreateModel(
            name='StationUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255)),
                ('station_name', models.CharField(max_length=255)),
                ('use_ym', models.CharField(max_length=6)),
                ('rental_count', models.IntegerField()),
                ('return_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_count', models.IntegerField(verbose_name='이용량')),
                ('use_date', models.CharField(max_length=8, verbose_name='대여날짜')),
                ('gender', models.CharField(max_length=10, null=True, verbose_name='성별')),
                ('age_range', models.CharField(max_length=10, null=True, verbose_name='연령대')),
                ('station', models.ForeignKey(db_column='station_id', on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='bike_data.station')),
            ],
        ),
    ]
