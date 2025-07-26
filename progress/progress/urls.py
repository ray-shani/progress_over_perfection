from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Option 1: Redirect the root path to your 'book_store' app's URLs
    path("", include("book_store.urls")), # This line makes '/' go to 'book_store' app

    path("admin/", admin.site.urls),
    path("books/", include("book_store.urls")),
]