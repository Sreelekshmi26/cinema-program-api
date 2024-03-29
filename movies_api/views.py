from django.shortcuts import render
from .models import Movies
from rest_framework import generics, permissions,status
from .serializers import MovieSerializer
from rest_framework.response import Response
from django.db.models import Sum, Count
# from .tasks import add
# Create your views here.


class MovieCreateView(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['post']
    
    def post(self, request):
        """
        Create a new movie.
        """
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            movie = serializer.save()
            return Response(
                {"movie": str(request.data['name'])},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieListView(generics.ListAPIView):
    """
    API view for retrieving a list of movies with order details.

    - List: GET method to retrieve a list of movies.


    Raises:
    - HTTP_200_OK: If the list of user profiles is successfully retrieved.

    Returns:
    - Response: A response containing a list of movies with associated ranks.
    ```
    """

    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Get the queryset of movies based on highest ranking.
        """
        queryset = Movies.objects.all().order_by('-rank')

        return queryset

    def list(self, request):
        """
        Retrieve a list of movies .
        """
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset, many=True)
        response_data = serializer.data
        return Response(response_data)