from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('birth', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=30, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'ordering': ['gender'],
            },
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_type', models.CharField(choices=[('s', 'serie'), ('f', 'film')], max_length=5)),
                ('title', models.CharField(max_length=80, unique=True)),
                ('original_title', models.CharField(blank=True, max_length=80, null=True)),
                ('seasons', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='tvfinder')),
                ('year', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('rating', models.FloatField()),
                ('summary', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('director', models.ManyToManyField(related_name='rel_directors', to='tv.Director')),
                ('gender', models.ManyToManyField(related_name='rel_genders', to='tv.Gender')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'ordering': ['title'],
            },
        ),
    ]
