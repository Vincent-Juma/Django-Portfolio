from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_location(self):
        self.save()
    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name       
    class Meta:
        ordering = ['name']

    def save_category(self):
        self.save()
    def update_category(self):
        self.update()
    def delete_category(self):
        self.delete()


class Image(models.Model):
    
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category) 
    image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  
    def update_image(self):
        self.update() 

    @classmethod
    def get_photos(cls,id):
        try:
           photos = Image.objects.get(id=id)
           return photos
        except DoesNotExist:
            return Image.objects.get(id=1)

        
    
         
    @classmethod
    def search_by_category(cls,search_term):
                category = Category.objects.filter(name__icontains=search_term).first()
                image = cls.objects.filter(category=category)
                return image

    @classmethod
    def search_by_location(cls,location):
                location = Location.objects.filter(name__icontains=location)
                image =cls.objects.filter(location=location)
                return image