from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def send_fullname(request):
    if request.method == "GET":

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "This service returns your data",
                "data": {"account": "mtn_gh", "name": "koko_seller"},
            },
            status=status.HTTP_200_OK,
        )

    elif request.method == "POST":
        name = request.data.get("name", None)
        job = request.data.get("job", None)
        data = f"Welcome {name} to Fido! You would work as a {job}"

        return Response(
            {"status": status.HTTP_201_CREATED, "data": data},
            status=status.HTTP_400_BAD_REQUEST,
        )


