from django.db import models
from django.contrib.auth.models import User  # ORM


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)  # 待辦事項標題
    text = models.TextField(
        blank=True
    )  # 待辦事項內容說明，blank=True指內容可以容許不填寫，否則原本是強制要寫
    created = models.DateField(auto_now_add=True)  # 待辦事項建立時間自動增加
    date_completed = models.DateTimeField(
        blank=True, null=True
    )  # 內容可以為空，物件可以為空
    important = models.BooleanField(
        default=False
    )  # 每一筆新建資料預設為不重要，除非打勾
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # 建立ORM關聯且CASCADE是指若主檔刪除了底下的關聯資料也一併被刪除

    completed = models.BooleanField(
        default=False
    )  # 有新增欄位一定要做資料表的makemigrations和migrate

    # 新增一個文字敘述直接顯示對應的文字內容
    # (self)指取model本身的項目ex:title/user
    def __str__(self):
        return f"{self.id}[{self.created}]-{self.title}-({self.user})"
