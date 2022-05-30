from django.db import models
from django.urls import reverse

def attachment_path(instance, filename):
    return "sestavy/" + str(instance.sestava.id_sestavy) + "/attachments/" + filename
    
def poster_path(instance, filename):
    return "sestavy/" + str(instance.id_sestavy) + "/poster/" + filename

class Adresa(models.Model):
    id_adresy = models.AutoField(primary_key=True)
    mesto = models.CharField(max_length=45, verbose_name="Město")
    ulice = models.CharField(max_length=45, verbose_name="Ulice")
    cislo_popisne = models.IntegerField(verbose_name="Číslo popisné")
    
    class Meta:
        ordering = ["mesto", "id_adresy"]

    def __str__(self):
        return f"{self.ulice} {self.cislo_popisne}, {self.mesto}"

class Vyrobce(models.Model):
    nazev = models.CharField(primary_key=True, max_length=20, verbose_name="Název")
    popis = models.TextField(blank=True, null=True, max_length=200, verbose_name="Popis")
    
    class Meta:
        ordering = ["nazev"]

    def __str__(self):
        return self.nazev

class Komponenty(models.Model):
    nazev = models.CharField(primary_key=True, max_length=50, verbose_name="Název")
    typ = models.CharField(max_length=20, verbose_name="Typ")
    cena = models.IntegerField(verbose_name="Cena")
    vyrobce_nazev = models.ForeignKey(Vyrobce, models.DO_NOTHING, verbose_name="Výrobce")
    
    class Meta:
        ordering = ["typ", "cena"]

    def __str__(self):
        return f"{self.vyrobce_nazev} {self.nazev}"

class Pracovnik(models.Model):
    id_pracovnika = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=45, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=45, verbose_name="Příjmení")
    telefon = models.CharField(max_length=45, verbose_name="Telefonní číslo")
    adresa = models.ForeignKey(Adresa, models.DO_NOTHING, verbose_name="Adresa bydliště")
    
    class Meta:
        ordering = ["prijmeni", "jmeno"]

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Zakaznik(models.Model):
    id_zakaznika = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=45, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=45, verbose_name="Příjmení")
    popis = models.TextField(blank=True, null=True, max_length=200, verbose_name="Telefonní číslo")
    adresa = models.ForeignKey(Adresa, models.DO_NOTHING, verbose_name="Adresa bydliště")
    
    class Meta:
        ordering = ["prijmeni", "jmeno"]

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Sestava(models.Model):
    id_sestavy = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=50, verbose_name="Název")
    #nazev = models.CharField(primary_key=True, max_length=50, verbose_name="Název")
    cena = models.IntegerField(verbose_name="Cena")
    popis = models.TextField(blank=True, null=True, max_length=200, verbose_name="Popis")
    sestavil = models.ForeignKey(Pracovnik, models.DO_NOTHING, verbose_name="Sestavil")
    skladasez = models.ManyToManyField(Komponenty, verbose_name="Skládá se z")
    nahled = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Náhledový obrázek")
    
    class Meta:
        ordering = ["nazev", "-cena"]

    def __str__(self):
        return self.nazev

class Faktura(models.Model):
    id_faktury = models.AutoField(primary_key=True)
    vyhotoveni = models.DateTimeField(verbose_name="Datum vyhotovení")
    cena = models.IntegerField(verbose_name="Cena")
    zakaznik = models.ForeignKey(Zakaznik, models.DO_NOTHING, verbose_name="Zákazník")
    sestava = models.ForeignKey(Sestava, models.DO_NOTHING, verbose_name="Sestava")
    
    class Meta:
        ordering = ["sestava","vyhotoveni"]

    def __str__(self):
        return f"{self.zakaznik} koupil {self.sestava}"

class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulek")
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="Soubor")
    TYPE_OF_ATTACHMENT = (('image', 'Image'),('video', 'Video'),('other', 'Other'),)
    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image', help_text='Vyberte obrázek', verbose_name="Typ přílohy")

    sestava = models.ForeignKey(Sestava, on_delete=models.CASCADE)

    class Meta:
        ordering = ["sestava"]

    def __str__(self):
        return f"{self.title}, ({self.type})"