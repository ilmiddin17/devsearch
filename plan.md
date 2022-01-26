MODELS

User
    -> username
    -> email
    -> first_name
    -> last_name
    -> is_staff
    -> is_active
    -> id

Profile
    -> user
    -> name
    -> email
    -> username
    -> headline
    -> bio
    -> location
    -> profile_image
    -> social_github
    -> social_twitter
    -> social_linkedin
    -> socail_website
    -> created
    -> id

Project
    -> owner
    -> title
    -> description
    -> featured_image
    -> demo_link
    -> source_code
    -> vote_ratio
    -> vote_count
    -> tags
    -> created
    -> id

Review
    -> project
    -> owner
    -> body
    -> value
    -> created
    -> id

Tag
    -> id
    -> name
    -> created

Skill
    -> id
    -> owner
    -> name
    -> description
    -> created

Message
    -> id
    -> sender
    -> recipient
    -> name
    -> email
    -> subject
    -> body
    -> is_read
    -> created