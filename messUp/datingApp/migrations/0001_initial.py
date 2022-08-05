# Generated by Django 4.0.5 on 2022-08-05 13:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodyType', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestsChoice', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('token', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_message', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SexualOrientation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zodiac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zodiac', models.CharField(choices=[('Capricon', 'Capricon'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces'), ('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
                ('height', models.IntegerField()),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField(default=18)),
                ('date_of_birth', models.DateField(default=datetime.date(1997, 10, 19))),
                ('longitude', models.FloatField(blank=True, default=0.0, null=True)),
                ('latitude', models.FloatField(blank=True, default=0.0, null=True)),
                ('bodyType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.bodytype')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingApp.country')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingApp.institute')),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.login')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingApp.profession')),
                ('sexualOrientation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingApp.sexualorientation')),
                ('zodiac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.zodiac')),
            ],
        ),
        migrations.CreateModel(
            name='PictureGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile_image', models.ImageField(default='user-default.png', upload_to='profiles/')),
                ('image1', models.ImageField(default='user-default.png', upload_to='profiles/')),
                ('image2', models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profiles/')),
                ('image3', models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profiles/')),
                ('image4', models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profiles/')),
                ('image5', models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profiles/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='MatchMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_check', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='datingApp.profile')),
                ('person2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='datingApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='InterestsID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('interest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.interests')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datingApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BlockProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_check', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='datingApp.profile')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='datingApp.profile')),
            ],
        ),
    ]
