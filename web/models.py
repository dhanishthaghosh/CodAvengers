from web import db, app


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    rating_value = db.Column(db.String(10), nullable=True)
    ratings_count = db.Column(db.String(10), nullable=True)
    per_night_cost = db.Column(db.String(10), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    booking_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"Hotel('{self.name}', '{self.address}', '{self.rating_value}', '{self.ratings_count}', '{self.per_night_cost}')"
