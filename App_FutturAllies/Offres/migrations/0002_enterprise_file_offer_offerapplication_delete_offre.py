# Generated by Django 4.2 on 2024-11-18 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Offres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('recruitment_email', models.EmailField(max_length=254)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=10)),
                ('website', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('founded_year', models.PositiveIntegerField(blank=True, null=True)),
                ('headquarters_location', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('company_culture', models.TextField(blank=True, null=True)),
                ('social_media_links', models.JSONField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('awards_and_recognition', models.JSONField(blank=True, null=True)),
                ('benefits_overview', models.TextField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('gridfs_id', models.CharField(max_length=255)),
                ('file_size', models.PositiveBigIntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('domain', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Job', 'Job'), ('Internship', 'Internship'), ('Other', 'Other')], max_length=20)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('education_level', models.CharField(blank=True, max_length=255, null=True)),
                ('experience_level', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship'), ('Freelance', 'Freelance'), ('Temporary', 'Temporary')], max_length=20)),
                ('benefits', models.TextField(blank=True, null=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Pending', 'Pending')], default='Open', max_length=20)),
                ('is_remote', models.BooleanField(default=False)),
                ('application_mode', models.CharField(choices=[('Online', 'Online'), ('Physical', 'Physical'), ('Both', 'Both')], default='Online', max_length=20)),
                ('online_submission', models.BooleanField(default=True)),
                ('physical_address', models.TextField(blank=True, null=True)),
                ('is_required_cv_doc', models.BooleanField(default=True)),
                ('is_required_ml_doc', models.BooleanField(default=False)),
                ('can_add_others_doc', models.BooleanField(default=False)),
                ('application_link', models.URLField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='Offres.enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='OfferApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('In Review', 'In Review')], default='Pending', max_length=20)),
                ('message', models.TextField(default="Je suis très intéressé(e) par cette offre et je suis convaincu(e) que mes compétences et mon expérience correspondent aux attentes de votre entreprise. J'aimerais avoir l'opportunité de discuter de cette offre plus en détail et de contribuer au succès de votre équipe.")),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('submitted_documents_ids', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='Offres.offer')),
            ],
        ),
        migrations.DeleteModel(
            name='Offre',
        ),
    ]
