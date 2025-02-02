# Generated by Django 5.1.5 on 2025-02-02 09:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0006_alter_faq_answer_es_alter_faq_answer_fr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_de',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_it',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ja',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ko',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_pt',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_zh',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ko',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_zh',
            field=models.TextField(blank=True, null=True),
        ),
    ]
