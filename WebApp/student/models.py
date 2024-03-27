from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class CourseInfo(models.Model):
    course_name=models.CharField(max_length=20)
    course_short_form=models.CharField(max_length=10)

    def __str__(self):
        return self.course_name+"("+self.course_short_form+")"

class BatchInfo(models.Model):
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=100)
    date_started = models.DateField()

    def __str__(self):
        return f"{self.batch_name}"             #{self.course.course_name} - 


class StudentInfo(models.Model):
    
    std_full_name=models.CharField(max_length=50)
    std_email=models.EmailField(unique=True)
    std_phone_no=models.CharField(max_length=13)
    std_address=models.TextField()
    std_qualification=models.CharField(max_length=10)
    std_year_of_passed_out=models.DateField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    std_gender = models.CharField(choices=gender_choice, max_length=10)
    std_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    course_type=models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    batch_type=models.ForeignKey(BatchInfo,on_delete=models.SET_NULL,null=True,blank=True)
    std_password=models.CharField(max_length=10,editable=False,default='123456')
    std_id=models.CharField(max_length=10,primary_key=True,editable=False)
    class Meta:
        unique_together = ["std_id", "course_type"]

    def __str__(self):
        return  self.std_full_name + "(" + self.std_id + ")"


@receiver(pre_save, sender=StudentInfo)
def generate_stdid(sender, instance, **kwargs):
    # Check if stdid is not already set
    if not instance.std_id:
        first_two_letters = str(instance.batch_type)
        count_with_same_prefix = StudentInfo.objects.filter(batch_type=instance.batch_type).count()
        # print("------------",f"{first_two_letters}{count_with_same_prefix :03d}")
        instance.std_id = f"{first_two_letters}{count_with_same_prefix + 1 :03d}"
        instance.std_password=f"{first_two_letters}{count_with_same_prefix + 1 :03d}"
        # print(len(instance.std_id))
#--------------
        user_exists = User.objects.filter(email=instance.std_email).exists()
        if not user_exists:
            # Create a new active user
            User.objects.create_user(
                username=instance.std_id,
                email=instance.std_email,
                password=instance.std_password,  # Set password if required
                is_active=True,
                # Add other user fields if necessary
            )

    