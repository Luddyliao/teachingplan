from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TeachingPlan
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# 交學計畫列表
class TeachingplanList(LoginRequiredMixin, ListView):
    model = TeachingPlan
    ordering = ['-id']      # 依 id 欄位反向排序(新的在前面)
    paginate_by = 3         # 設定每頁最多顯示的資料筆數
    
# 新增教學計畫
class TeachingplanCreate(LoginRequiredMixin, CreateView):
    model = TeachingPlan
    fields = '__all__'            # 自動產生表單時僅顯示 content 欄位
    success_url = '/teachingplan/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 修改教學計劃
class TeachingplanUpdate(LoginRequiredMixin, UpdateView):
    model = TeachingPlan
    fields = ['content']            # 自動產生表單時僅顯示 content 欄位
    success_url = '/teachingplan/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 刪除教學計劃
class TeachingplanDelete(LoginRequiredMixin, DeleteView):
    model = TeachingPlan
    success_url = '/teachingplan/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'confirm_delete.html'


class TeachingplanSemester(ListView):
    model = TeachingPlan
    template_name = 'class.html'
    
    def get_queryset(self):
        return TeachingPlan.objects.filter(
            seme = self.kwargs['seme']
        )

class TeachingplanSemesterClass(ListView):
    model = TeachingPlan
    template_name = 'class.html'
    
    def get_queryset(self):
        return TeachingPlan.objects.filter(
            seme = self.kwargs['seme'], 
            cclass = self.kwargs['cid']
        )


   
    
