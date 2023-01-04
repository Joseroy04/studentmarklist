from django.db import models

# Create your models here.
class Pedagogy(models.Model):
    subject = models.CharField(verbose_name="Pedagogy Subjects",max_length=30,null=False)
    class Meta:
        verbose_name = ("Pedagogy Subjects")
    def __str__(self):
        return self.subject
    
    
class Deportment(models.Model):
    name = models.CharField(verbose_name="Deportment ",max_length=30,null=False)
    class Meta:
        verbose_name = ("Deportment ")
    def __str__(self):
        return self.name
    
class studentData(models.Model):
    name = models.CharField(verbose_name="Student Name ", max_length=50,null=False,unique=False)
    applicationNo =models.IntegerField(verbose_name="Application number",null=False,unique=True,primary_key=True)
    dob = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False,)
    deportment = models.ForeignKey("Deportment",on_delete=models.CASCADE,verbose_name=("Deportment Name"))
    pedagogy = models.ForeignKey("app1.Pedagogy", verbose_name=("pedagogy subject"), on_delete=models.CASCADE)
    
    s1T = models.IntegerField(verbose_name="Educational Psychology theary ",null=False )
    s2T = models.IntegerField(verbose_name="Contemporay India and Education theary ",null=False )
    s3T = models.IntegerField(verbose_name="Teaching and Learing theary ",null=False )
    s4T = models.IntegerField(verbose_name="Language across the Curriculum theary ",null=False )
    s5T = models.IntegerField(verbose_name="Pedagogy Subject theary ",null=False )
    
    s1A= models.IntegerField(verbose_name="Educational Psychology Assignment ",null=True,blank=True )
    s2A= models.IntegerField(verbose_name="Contemporay India and Education Assignment ",null=False )
    s3A= models.IntegerField(verbose_name="Teaching and Learing Assignment ",null=False )
    s4A= models.IntegerField(verbose_name="Language across the Curriculum Assignment ",null=False )
    s5A= models.IntegerField(verbose_name="Pedagogy Subject Assignment ",null=False )
    
    s1LS= models.IntegerField(verbose_name="Educational Psychology Late Submission Penalty Mark ",null=False ,default=0)
    s2LS= models.IntegerField(verbose_name="Contemporay India and Education Late Submission Penalty Mark ",null=False,default=0 )
    s3LS= models.IntegerField(verbose_name="Teaching and Learing Late Submission Penalty Mark ",null=False ,default=0)
    s4LS= models.IntegerField(verbose_name="Language across the Curriculum Late Submission Penalty Mark ",null=False,default=0 )
    s5LS= models.IntegerField(verbose_name="Pedagogy Subject Late Submission Penalty Mark ",null=False ,default=0)
    
    s1LS= models.IntegerField(verbose_name="Educational Psychology Late Submission Penalty Mark ",null=False ,default=0)
    s2LS= models.IntegerField(verbose_name="Contemporay India and Education Late Submission Penalty Mark ",null=False,default=0 )
    s3LS= models.IntegerField(verbose_name="Teaching and Learing Late Submission Penalty Mark ",null=False ,default=0)
    s4LS= models.IntegerField(verbose_name="Language across the Curriculum Late Submission Penalty Mark ",null=False,default=0 )
    s5LS= models.IntegerField(verbose_name="Pedagogy Subject Late Submission Penalty Mark ",null=False ,default=0)
    
    
    s1Total = models.IntegerField(verbose_name="Educational Psychology Total ",null=True,blank=True,default=0 )
    s2Total = models.IntegerField(verbose_name="Contemporay India and Education Total ",null=True,blank=True,default=0 )
    s3Total = models.IntegerField(verbose_name="Teaching and Learing Total ",null=True,blank=True ,default=0)
    s4Total = models.IntegerField(verbose_name="Language across the Curriculum Total ",null=True,blank=True ,default=0)
    s5Total = models.IntegerField(verbose_name="Pedagogy Subject Total ",null=True,blank=True,default=0 )
    
    total = models.IntegerField(verbose_name="Total Mark",null=True,blank=True,default=0)
    average = models.DecimalField(verbose_name="Average ",null=True,blank=True,max_digits=10,decimal_places=3,default=0)
    def save(self, *args, **kwargs):
       self.s1Total = self.s1A +self.s1LS +self.s1T
       self.s2Total = self.s2A +self.s2LS +self.s2T
       self.s3Total = self.s3A +self.s3LS +self.s3T
       self.s4Total = self.s4A +self.s4LS +self.s4T
       self.s5Total = self.s5A +self.s5LS +self.s5T
       
       
       self.total = self.s1Total+self.s2Total+self.s3Total+self.s4Total+self.s5Total
       
       self.average = self.total / 5
       
       super(studentData, self).save(*args, **kwargs) # Call the real save() method
    class Meta:
        verbose_name = ("studentdata")
        verbose_name_plural = ("studentdatas")

    def __str__(self):
        return self.name

