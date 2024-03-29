# Generated by Django 2.2.4 on 2019-10-05 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data_nacimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAbertura', models.DateTimeField(auto_now_add=True)),
                ('interessados', models.ManyToManyField(related_name='interessados', to='app_correcaoG1.Pessoa')),
                ('investigados', models.ManyToManyField(related_name='investigados', to='app_correcaoG1.Pessoa')),
                ('local', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_correcaoG1.Pessoa')),
                ('Matricula', models.CharField(max_length=15, verbose_name='N° de Matricula')),
                ('Funcao', models.CharField(max_length=20, verbose_name='Função')),
            ],
            bases=('app_correcaoG1.pessoa',),
        ),
        migrations.CreateModel(
            name='PortariaDeInstauracao',
            fields=[
                ('documento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_correcaoG1.Documento')),
                ('dataMov', models.DateField(auto_now_add=True)),
                ('texto', models.TextField(blank=True, null=True, verbose_name='Breve texto')),
            ],
            bases=('app_correcaoG1.documento',),
        ),
        migrations.CreateModel(
            name='Tramitacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datamov', models.DateField(auto_now_add=True)),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Departamento')),
                ('origem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origem', to='app_correcaoG1.Departamento')),
                ('processo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Processo')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15, verbose_name='Titulo')),
                ('data', models.DateField(blank=True, null=True)),
                ('processo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Processo')),
            ],
        ),
        migrations.AddField(
            model_name='processo',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Funcionario'),
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('documento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_correcaoG1.Documento')),
                ('dataDeEnvio', models.DateField(blank=True, null=True, verbose_name='Data: ')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_correcaoG1.Departamento')),
            ],
            bases=('app_correcaoG1.documento',),
        ),
    ]
