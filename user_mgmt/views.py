import csv
import requests
from django.http import HttpResponse, HttpRequest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user_mgmt.models import *
from user_mgmt.serializers import *


class BaseUserViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer


class InstitutionViewSet(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class FilterInstitutionViewSet(generics.RetrieveAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

    # renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        institution_by_name = Institution.objects.filter(name__icontains='name')  # .filter(research_institution=False)
        serializer = InstitutionSerializer(institution_by_name, many=True, context={'request': request})
        return Response({"Institution_by_name": serializer.data}, template_name='institutions/institutions_search.html')


class ExportCSVStudents(APIView):
    # https://stackoverflow.com/questions/56877025/django-rest-framework-how-i-can-make-export-model-in-csv
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)
        for student in Student.objects.all():
            assigned_courses = CourseParticipant.objects.filter(student=student)
            completed_courses = assigned_courses.filter(completed=True)

            row = [
                student.full_name,
                assigned_courses.count(),
                completed_courses.count()
            ]

            writer.writerow(row)

        return response


# class ImportDataView(APIView):
# # https://www.youtube.com/watch?v=UKE5yQAmg0k
# # https://stackoverflow.com/questions/69119309/pass-row-data-from-csv-to-api-and-append-results-to-an-empty-csv-column

#     headers = {
#         'Authorization': 'token',
#         'Content-Type': 'application/json; charset=utf-8',
#     }
#
#     with open('survey_results_public.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data = str([row])
#
#     response = requests.post(
#         'https://localhost:8000/imposrt_data',
#         headers=headers,
#         data=data
#     )


class RegisterInstitution(generics.CreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

    def create(self, validated_data):
        institution = Institution(**validated_data)
        institution.save()
        return institution


class UpdateBaseUser(generics.UpdateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UpdateSerializer

    def update(self, validated_data):
        user = BaseUser(**validated_data)
        user.save()
        return user


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
