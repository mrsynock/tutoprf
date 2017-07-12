from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def creat(self, validated_data):
        """
        Create and retrun a nex 'snippet', selon la validation
        """
        return Snippet.objects.create(**validated_data)
