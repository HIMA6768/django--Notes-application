from django .urls import path
from .views import homepage,about,notesave,notedelete,noteedit,updatenote,viewnote,signup,saveuser,loginuser,loginchk,logoutuser
urlpatterns=[
    path("",homepage,name="homepage"),
    path("about",about,name="about"),
    path("notes",notesave,name="notesave"),
    path("delete/<int:id>",notedelete,name="delete"),
    path("editnote/<int:id>",noteedit,name="edit"),
    path("updatenote/<int:id>",updatenote,name="update"),
    path("viewnote/<int:id>",viewnote,name="view"),
    path("signup",signup,name='signup'),
    path("saveuser",saveuser,name="saveuser"),
    path("login",loginuser,name="login"),
    path("loginchk",loginchk,name="loginchk"),
    path("logout",logoutuser,name="logout")


]