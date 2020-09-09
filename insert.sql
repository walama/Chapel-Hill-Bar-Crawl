USE bar_crawl;
/*  comment out table you are not using*/

-- INSERT INTO bars(bar, vibes, comments)
-- VALUES
--     ("Blue Horn", 3, "Irish Pub"),
--     ("Zoggs", 5, "Pool Hall, get the random beer deal");

INSERT INTO drinks(drink, drink_type, price, ounces, apv, bar_id)
VALUES
    ("Miller Lite", "beer", 3.0, 12, 3.5, 5),
    ("Bud Light", "beer", 2.5, 12, 3.5, 6),
    ("Coors Light", "beer", 3.25, 12, 3.5, 3),
    ("Bud Light", "beer", 3.5, 12, 3.5, 3),
    ("Coors Light", "beer", 4.25, 12, 3.5, 4);