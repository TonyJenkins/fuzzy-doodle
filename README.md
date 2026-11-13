# The WAT Dog Club

## File Structure

The Django "project" is in the `config` directory.

Django apps are intended to live in the `apps` directory. Note that
this means that their names have to be qualified in the code
with the `apps` prefix.

The bones (see what I did there?) of an app to list all the dogs registered
in the club can be found in the `dog_roster` folder below `apps`.

There is also a very basic Home Page app in `apps/home_page`.

## Endpoints

As you work on this project, you will add a number of endpoints to the
template app. Your app(s) should implement the following endpoints **with
the names and format as shown**. These will be used in the
automated testing. **If you do not follow these, you will not get any marks
for the features implemented**.

| Endpoint                      | Description                    |
|-------------------------------|--------------------------------|
| /                             | Home page                      |
| /dogs                         | Dog list                       |
| /dogs/agility                 | Agility Dogs                   |
| /dogs/leaderboard             | Leaderboard                    |
| /dogs/dog/\<int:dog_id\>      | Individual Dog Page            |
| /dogs/dog/\<int:dog_id\>/like | Like a Dog for the Leaderboard |

All of the above are GET requests. (This is the only type of request
that you need to implement.)

## Tasks

First, create your database, and use the provided test fixture to populate it
with a collection of dogs. Use the Django Admin to see the data. Then examine 
the three URL definition files in the project (one in `config`, one in each app) 
to see what routes are defined.

You should be able to find a very basic home page, an HTML list of all the dogs
(with very basic CSS), and a buggy page to show details of one dog. (This last
is intentionally broken).

There is a video on MyBeckett to guide you through the initial setup. (It
uses a slightly earlier version of the template repo, but everything is
basically the same.)

The tasks for the assignment are below. You are free to use any design for
your site, but remember that this is not a web design assignment. You should
aim for a front-end that "works", but there is no need for eye candy. The 
code in the back-end you create is much more important.

### Dog Details

Fix the broken view for displaying a single dog, and add a link to each 
dog's detail page from the list view. *Hint: Look in the model for something 
that will help here.*

Add to the HTML and CSS for the full listing to present the data better. Use "cards"
for each dog if you want. Format the individual "dog details pages" in a way that complements
the main display. Make sure you add a way to get from the details page back to the
main listing.

There are 100 dogs in the fixture, so it will be best to **Paginate** the display so
that, say, 10 are displayed at once. So do that.

And obviously there should be an image of each dog. Again, look in the model for something
that will provide the URL of a placeholder image.

### Home Page

Create a home page for the Dog Club. The design should be similar to the "Dog List", but 
does not have to be the same. Have a clear link from it to the "Dog List".

Add to the home page a random "dog fact". To do this, create a model and tweak the home
page view (it has been written to allow this to be done easily). Then use Copilot or 
similar to create a pool of about 50 doggy facts. Modify the view and template to select
and display a random fact from this pool. *Hint: Remember to "migrate" your changes.*

### Pimp the Admin

Since we now have two models (and probably two apps) this is a good time to make sure the admin
screens are fit for purpose. So spend some time deciding which fields should be searchable, 
which should be filters, and so on. If you check PyPi, you will also find packages there that
will allow you a lot of control over the look and feel of the admin screens.

### Agility Class

Some of the dogs partake of an agility class. Add a link on the home page that goes to a listing
of just these dogs. You can use the same design as the main listing, but you will probably want
to change the page titles, headings, and so on.

*Hint: There are several ways to do this, but you will need to tweak the model in the existing app.*

### Like a Dog

Members of the Dog Club can vote for their favourites. Add a link to each dog in the listing to allow 
users to like a dog. And add the number of likes to the display for each hound. You will obviously also
need to apply a further tweak to the model in order to store this new value.

Then add a link to a "leaderboard" to the home page that lists the current top ten "liked" dogs, in descending 
order of likes.

*Hint: "likes" are not in the test fixture, so set a default of zero, and use the admin screens to 
add some likes to the dogs. You can then use `dumpdata` to save your new fixture.*

### Authorisation

Now, change the site so that only logged-in members can like dogs. 

There is no need to add a registration screen (but you can if you want to) - just use the 
existing admin screens to create some users.
You *will* need to add a login system, and obviously a corresponding logout. *Hint: This
is nowhere near as complicated as it sounds - Django will do all the heavy lifting
for you.*

For that extra touch, add the logged-in user's name to the Home Page in some
sort of cheery welcome message.

### Bells and Whistles

You may, of course, add anything else relevant that you want to.

## Video Specification

### Length

You should aim for a video of 10 minutes duration. Videos longer than 11 minutes will be
marked based on the first 10 minutes, with the rest not being watched. Videos significantly
shorter than 10 minutes long will be penalised.

### Content

The video should demonstrate, **in this order**:

1. The Home Page and the Dog Listing.
2. The Individual Dog Pages.
3. The Agility Dogs.
4. The Leaderboard.
5. The "like" functionality, and how it alters the Leaderboard.
6. The admin screens.

If these are not presented in this order, significant marks will be lost.
