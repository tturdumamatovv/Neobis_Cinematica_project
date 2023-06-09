# Generated by Django 4.2.1 on 2023-05-19 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_seat', models.IntegerField()),
                ('number_of_row', models.IntegerField()),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('payment_methods', models.IntegerField(choices=[(1, 'Bank-card'), (2, 'Balance.kg'), (3, 'Элсом')])),
                ('club_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.clubcard')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.orders')),
                ('seats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.seats')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.showtime')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickettype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('rate', models.IntegerField(blank=True, choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.seats')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.showtime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
