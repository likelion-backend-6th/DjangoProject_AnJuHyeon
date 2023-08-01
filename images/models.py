from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked', blank=True)
    class Meta:
        indexes = [models.Index(fields=['-created'])]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # 객체의 slug 필드가 비어있으면 (not self.slug)
        # slugify 함수를 사용하여 self.title의 값을 기반으로 새로운 슬러그를 생성
        if not self.slug:
            self.slug = slugify(self.title)

        # 부모 클래스인 models.Model의 save 메서드를 호출하여 객체를 실제로 저장
        super().save(*args, **kwargs)