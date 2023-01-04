# Generated by Django 4.1.5 on 2023-01-04 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_pedagogy_studentdata_delete_studentdatas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deportment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Deportment ')),
            ],
            options={
                'verbose_name': 'Deportment ',
            },
        ),
        migrations.AddField(
            model_name='studentdata',
            name='average',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Average '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='s1Total',
            field=models.IntegerField(default=0, null=True, verbose_name='Educational Psychology Total '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='s2Total',
            field=models.IntegerField(default=0, null=True, verbose_name='Contemporay India and Education Total '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='s3Total',
            field=models.IntegerField(default=0, null=True, verbose_name='Teaching and Learing Total '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='s4Total',
            field=models.IntegerField(default=0, null=True, verbose_name='Language across the Curriculum Total '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='s5Total',
            field=models.IntegerField(default=0, null=True, verbose_name='Pedagogy Subject Total '),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='total',
            field=models.IntegerField(default=0, null=True, verbose_name='Total Mark'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='deportment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.deportment', verbose_name='Deportment Name'),
        ),
    ]
