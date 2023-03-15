from import_export import resources

from .models import CompetitionData, TrainingData


class TrainingDataResource(resources.ModelResource):
    class Meta:
        model = TrainingData


class CompetitionDataResource(resources.ModelResource):
    class Meta:
        model = CompetitionData
