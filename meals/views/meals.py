'''Stores views.'''

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Serializers
from meals.serializers import MealModelSerializer

# Models
from meals.models import Meal
from users.models import Store



class MealViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    '''Meals view set.
    
    #################################################################################
    Http methods and the URLs:

    GET             /stores/                        (list Stores)
    POST            /stores/                        (create Store)
    PUT             /stores/                        (update Store info)
    PATCH           /stores/                        (partial update Store info)
    ######################################################################################
    '''

    serializer_class = MealModelSerializer
    lookup_field = 'slugname'
    search_fields = ('slugname', 'name')


    # Method call every time this MealViewSet is instanced
    def dispatch(self, request, *args, **kwargs):
        '''Verify that the store exists.
        Add the URL input <store_slugname> to the Meal model field store(FK).
        '''

        store_slugname = kwargs['store_slugname']
        self.store = get_object_or_404(Store, store_slugname=store_slugname)

        return super(MealViewSet, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        '''Get Store's available meals'''

        return Meal.objects.filter(
            store=self.store,
            is_available=True
        )
    
    def create(self, request, *args, **kwargs):
        '''Assign Meal to a Store (received in the URL input <store_slugname>)
        '''
        store = self.store # Got from the dispatcher
        request.data['store'] = store
        serializer = MealModelSerializer(
            store,
            data=request.data
        )
        # import pdb; pdb.set_trace()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)







      
      
        # store_slugname = kwargs['store_slugname']
        # store = Store.objects.get(store_slugname=store_slugname)
        # request.data['store'] = store['pk']
        