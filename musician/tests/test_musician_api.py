from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from musician.models import Musician
from musician.serializers import MusicianSerializer

MUSICIAN_URL = reverse("musician:manage-list")


class MusicianApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.first_musician = Musician.objects.create(
            first_name="Joseph",
            last_name="Green",
            instrument="the guitar",
            age=17,
        )
        self.second_musician = Musician.objects.create(
            first_name="Robert",
            last_name="Brown",
            instrument="the guitar",
            age=28,
        )

    def test_age_has_min_value(self):
        payload = {
            "first_name": "Jim",
            "last_name": "Greg",
            "instrument": "the violin",
            "age": 10,
        }

        response = self.client.post(MUSICIAN_URL, payload)
        musicians = Musician.objects.all()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(musicians.count(), 2)

    def test_get_musicians(self):
        musicians = self.client.get(MUSICIAN_URL)
        serializer = MusicianSerializer(Musician.objects.all(), many=True)
        self.assertEqual(musicians.status_code, status.HTTP_200_OK)
        self.assertEqual(musicians.data, serializer.data)

    def test_post_musicians(self):
        musicians = self.client.post(
            MUSICIAN_URL,
            {
                "first_name": "Bob",
                "last_name": "Yellow",
                "instrument": "the guitar",
                "age": 47,
            },
        )
        db_musicians = Musician.objects.all()
        self.assertEqual(musicians.status_code, status.HTTP_201_CREATED)
        self.assertEqual(db_musicians.count(), 3)
        self.assertEqual(db_musicians.filter(first_name="Bob").count(), 1)

    def test_get_musician(self):
        response = self.client.get(f"{MUSICIAN_URL}{self.first_musician.id}/")
        serializer = MusicianSerializer(self.first_musician)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertIn("is_adult", response.data)

    def test_get_invalid_musician(self):
        response = self.client.get(f"{MUSICIAN_URL}50/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_musician(self):
        self.client.put(
            f"{MUSICIAN_URL}1/",
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "instrument": "the violin",
                "age": 22,
            },
        )
        db_musician = Musician.objects.get(id=1)
        self.assertEqual(
            [
                db_musician.first_name,
                db_musician.last_name,
                db_musician.instrument,
                db_musician.age,
            ],
            ["Bob", "Smith", "the violin", 22],
        )

    def test_put_invalid_musician(self):
        response = self.client.put(
            f"{MUSICIAN_URL}50/",
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "instrument": "the violin",
                "age": 22,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_musician(self):
        response = self.client.patch(
            f"{MUSICIAN_URL}1/",
            {
                "first_name": "Leyla",
            },
        )
        db_musician = Musician.objects.get(id=1)
        self.assertEqual(db_musician.first_name, "Leyla")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_musician(self):
        response = self.client.patch(
            f"{MUSICIAN_URL}50/",
            {
                "first_name": "Leyla",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_musician(self):
        response = self.client.delete(
            f"{MUSICIAN_URL}1/",
        )
        db_musician_id_1 = Musician.objects.filter(id=1)
        self.assertEqual(db_musician_id_1.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_musician(self):
        response = self.client.delete(
            f"{MUSICIAN_URL}50/",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
