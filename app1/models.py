from django.db import models

# Create your models here.
class Pedagogy(models.Model):
    subject = models.CharField(verbose_name="Pedagogy Subjects",max_length=30,null=False)
    class Meta:
        verbose_name = ("Pedagogy Subjects")
    def __str__(self):
        return self.subject
class studentData(models.Model):
    name = models.CharField(verbose_name="Student Name ", max_length=50,null=False,unique=False)
    applicationNo =models.IntegerField(verbose_name="Application number",null=False,unique=True,primary_key=True)
    dob = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False,)
    deportment = models.CharField(verbose_name="Deportment",max_length=50,null=False)
    pedagogy = models.ForeignKey("app1.Pedagogy", verbose_name=("pedagogy subject"), on_delete=models.CASCADE)
    
    s1T = models.IntegerField(verbose_name="Educational Psychology theary ",null=False )
    s2T = models.IntegerField(verbose_name="Contemporay India and Education theary ",null=False )
    s3T = models.IntegerField(verbose_name="Teaching and Learing theary ",null=False )
    s4T = models.IntegerField(verbose_name="Language across the Curriculum theary ",null=False )
    s5T = models.IntegerField(verbose_name="Pedagogy Subject theary ",null=False )
    
    s1A= models.IntegerField(verbose_name="Educational Psychology Assignment ",null=True )
    s2A= models.IntegerField(verbose_name="Contemporay India and Education Assignment ",null=False )
    s3A= models.IntegerField(verbose_name="Teaching and Learing Assignment ",null=False )
    s4A= models.IntegerField(verbose_name="Language across the Curriculum Assignment ",null=False )
    s5A= models.IntegerField(verbose_name="Pedagogy Subject Assignment ",null=False )
    
    s1LS= models.IntegerField(verbose_name="Educational Psychology Late Submission Penalty Mark ",null=False ,default=0)
    s2LS= models.IntegerField(verbose_name="Contemporay India and Education Late Submission Penalty Mark ",null=False,default=0 )
    s3LS= models.IntegerField(verbose_name="Teaching and Learing Late Submission Penalty Mark ",null=False ,default=0)
    s4LS= models.IntegerField(verbose_name="Language across the Curriculum Late Submission Penalty Mark ",null=False,default=0 )
    s5LS= models.IntegerField(verbose_name="Pedagogy Subject Late Submission Penalty Mark ",null=False ,default=0)
    
    class Meta:
        verbose_name = ("studentdata")
        verbose_name_plural = ("studentdatas")

    def __str__(self):
        return self.name

