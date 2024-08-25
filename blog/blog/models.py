from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
    def copy(self):
        new_blog_post = BlogPost(title=self.title, body=self.body, author=self.author, date_created=timezone.now())
        new_blog_post.save()
        
        for comment in self.comments.all():
            Comment.objects.create(blog_post=new_blog_post, text=comment.text)
            
        return new_blog_post.id
        
    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    
    def __str__(self):
        return self.text