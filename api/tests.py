from django.test import TestCase
#from .models import EventOrginizers
# from .models import EventUsers
# from .models import Events
from .models import Users
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):

    def setUp(self):
        # self.eventOrginizers_event_id = 23
        # self.eventOrginizers_user_id = 23
        # self.eventOrginizers = EventOrginizers(event_id=self.eventOrginizers_event_id, user_id=self.eventOrginizers_user_id)

        # self.eventUsers_event_id = 2
        # self.eventUsers_user_id = 3
        # self.eventUsers_status = 12
        # self.eventUsers = EventUsers(event_id=self.eventUsers_event_id,user_id=self.eventUsers_user_id,status=self.eventUsers_status)
        #
        self.Users_name = "Vlad"
        self.Users_age = 20
        self.Users_email = "vlad@gmail.com"
        self.Users_number = 45354
        self.users = Users(name=self.Users_name,age=self.Users_age,email=self.Users_email,number=self.Users_number)

        # self.Events_initializer = 100
        # self.Events_location = "vladvlad"
        # self.Events_title = "vlad"
        # self.events = Events(initializer=self.Events_initializer,location=self.Events_location,title=self.Events_title)


    # def test_model_can_create_a_eventOrginizers(self):
    #     old_count = EventOrginizers.objects.count()
    #     self.eventOrginizers.save()
    #     new_count = EventOrginizers.objects.count()
    #     self.assertNotEqual(old_count, new_count)

    # def test_model_can_create_a_eventUsers(self):
    #     old_count = EventUsers.objects.count()
    #     self.eventUsers.save()
    #     new_count = EventUsers.objects.count()
    #     self.assertNotEqual(old_count, new_count)
    #
    def test_model_can_create_a_Users(self):
        old_count = Users.objects.count()
        self.users.save()
        new_count = Users.objects.count()
        self.assertNotEqual(old_count, new_count)
    #
    # def test_model_can_create_a_Events(self):
    #     old_count = Events.objects.count()
    #     self.events.save()
    #     new_count = Events.objects.count()
    #     self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.Users_data = {'name':"VLad",'age':20,'email':"vlad@gmail.com",'number': 5397897,}
        self.response = self.client.post(
            reverse('create'),
            self.Users_data,
            format="json")


    def test_api_can_create_a_Users(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_Users(self):
        """Test the api can get a given bucketlist."""
        users = Users.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': users.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, users)

    def test_api_can_update_Users(self):
        """Test the api can update a given bucketlist."""
        change_users = {'name':"VLad",'age':20,'email':"vlad@gmail.com",'number': 5397897,}
        users = Users.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': users.id}),
            change_users, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_Users(self):
        """Test the api can delete a bucketlist."""
        users = Users.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': users.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)