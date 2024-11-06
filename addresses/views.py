from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Address
from .serializers import AddressSerializer
from .utils import geocode_address


@api_view(['POST'])
def set_address(request):
    address = request.data.get('address')
    if not address:
        return Response(
            {'error': 'Address is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    geo_data = geocode_address(address)
    if geo_data is None:
        return Response(
            {'error': 'Failed to geocode address'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    address_obj = Address.objects.create(
        city=geo_data['city'],
        street=geo_data['street'],
        building=geo_data['building']
    )

    return Response(
        AddressSerializer(address_obj).data,
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def get_addresses(request):
    city = request.query_params.get('city')
    street = request.query_params.get('street')
    building = request.query_params.get('building')

    addresses = Address.objects.all()
    if city:
        addresses = addresses.filter(city__icontains=city)
    if street:
        addresses = addresses.filter(street__icontains=street)
    if building:
        addresses = addresses.filter(building__icontains=building)

    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_address_detail(request, address_id):
    try:
        address = Address.objects.get(id=address_id)
    except Address.DoesNotExist:
        return Response(
            {'error': 'Address not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = AddressSerializer(address)
    return Response(serializer.data, status=status.HTTP_200_OK)
