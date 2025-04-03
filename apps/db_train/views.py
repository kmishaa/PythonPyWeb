from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        obj = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        authors = Author.objects.filter(self_esteem__exact=obj['max_self_esteem'])
        # print(authors)
        self.answer1 = authors

        obj = Author.objects.aggregate(max_entries=Max('entries'))
        author = Author.objects.get(entries=obj['max_entries'])
        # print(author)
        self.answer2 = author

        obj = Entry.objects.filter(Q(tags__name='Кино') | Q(tags__name='Музыка'))
        # print(obj)
        self.answer3 = obj

        obj = Author.objects.filter(gender='ж').count()
        # print(obj)
        self.answer4 = obj

        obj = Author.objects.filter(status_rule=True).count()
        total = Author.objects.count()
        # print(int(obj/total*100), "%")
        self.answer5 = int(obj/total*100)

        obj = Author.objects.filter(authorprofile__stage__range=(1, 5))
        # print(obj)
        self.answer6 = obj

        obj = Author.objects.aggregate(max_age=Max('age'))
        author = Author.objects.get(age=obj['max_age'])
        # print(author)
        self.answer7 = obj['max_age']

        obj = Author.objects.exclude(phone_number__isnull=True).count()
        # print(obj)
        self.answer8 = obj

        obj = Author.objects.filter(age__lt=25)
        # print(obj)
        self.answer9 = obj

        result = []
        for auth in Author.objects.all():
            print(len(auth.entries.all()))
            obj = Entry.objects.filter(author=auth).count()
            # print(auth, "написал",obj, "статей")
            result.append({"username":auth, "count":obj})


        self.answer10 = result










        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}  # Создайте здесь запросы к БД
        return render(request, 'train_db/training_db.html', context=context)

