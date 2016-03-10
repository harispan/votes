__author__ = 'consultadd66'

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from tixdo.third_party_apps.votes.models import Vote
from django.core.urlresolvers import reverse


class CreateVoteTest(APITestCase):

    def setUp(self):
        self.data = {'content_type_id': 1, 'object_id': 1, 'user_id': 1}

    def test_can_create_show(self):
        response = self.client.post(reverse('vote-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadVoteTest(APITestCase):
    def setUp(self):
        self.vote = Vote.objects.create(content_type_id=1, object_id=1, user_id=1)

    def test_can_read_show_list(self):
        response = self.client.get(reverse('vote-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_show_detail(self):
        response = self.client.get(reverse('vote-detail', args=[self.vote.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateVoteTest(APITestCase):
    def setUp(self):
        self.vote = Vote.objects.create(content_type_id=1, object_id=1, user_id=1)

    def test_can_update_show(self):
        response = self.client.put(reverse('vote-detail', args=[self.vote.id]), {'user_id': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteVoteTest(APITestCase):
    def setUp(self):
        self.vote = Vote.objects.create(content_type_id=1, object_id=1, user_id=1)

    def test_can_delete_show(self):
        response = self.client.delete(reverse('vote-detail', args=[self.vote.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)