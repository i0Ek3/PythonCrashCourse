#!/usr/bin/env python
# coding=utf-8

#create a null list confirmed and unconfirmed to storage users
confirmed_users = []
unconfirmed_users = ['annabel','leon','bill','joe']

#verify users and add users to confirmed list and delete users in unconfirmed list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title() + "...")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())
