from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        new_blog_post = BlogPost.objects.create(
            title=self.title, body=self.body, author=self.author)
        for comment in Comment.objects.filter(blog_post=self):
            Comment.objects.create(
                blog_post=new_blog_post, text=comment.text)
        return new_blog_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, models.CASCADE)
    text = models.CharField(max_length=500)
