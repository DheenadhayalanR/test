from django.urls import path
from .views import SendFriendRequestView, RespondFriendRequestView, ListFriendsView, ListPendingRequestsView

urlpatterns = [
    path('request/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('request/<int:request_id>/', RespondFriendRequestView.as_view(), name='respond-friend-request'),
    path('list/', ListFriendsView.as_view(), name='list-friends'),
    path('pending/', ListPendingRequestsView.as_view(), name='list-pending-requests'),
]
