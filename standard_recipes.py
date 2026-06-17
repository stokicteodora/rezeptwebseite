# File: standard_recipes.py
# Author: Teodora Stokic
# Date: 05.06.2026
# Content: Standard recipes to enter into the database

from app import recipe_app, db, Recipe, Ingredient, Preparation, Category

with recipe_app.app_context():
    if Recipe.query.count() == 0:

        # Recipe 1
        category = Category(name='Dessert')
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Mango Float',
            description='Mango Float ist ein beliebtes philippinisches Schichtdessert, das ohne Backen zubereitet wird. Es überzeugt durch seine cremige Leichtigkeit und den erfrischenden Mangogeschmack, was es zum idealen Dessert für warme Tage macht. Inspiriert von der traditionellen Langka Float mit Jackfrucht, hat sich die Mango-Variante seit den 1980er-Jahren als Klassiker für Feste und Familienfeiern auf den Philippinen etabliert.',
            image='mango_float.png',
            preparation_time=130,
            portions=4,
            difficulty='Einfach',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Mango (geschält und in Würfel geschnitten)', quantity=300, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Schlagsahne', quantity=100, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Frischkäse', quantity=80, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Zucker', quantity=50, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Kekse', quantity=100, measurement_unit='g', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='In einer Schüssel Schlagsahne, Frischkäse und Zucker cremig verrühren.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Butterkekse grob zerbröseln und eine Schicht davon in ein Glas geben.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Eine Schicht Creme darauf verteilen, dann Mangostücke hinzufügen.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Die Schichten aus Keksbröseln, Creme und Mango abwechselnd fortsetzen, bis alle Zutaten aufgebraucht sind.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Mit einer Cremeschicht abschliessen und nach Belieben mit Mangostücken oder Keksbröseln bestreuen.', recipe_id=recipe.id),
            Preparation(step_number=6, description='Das Dessert mindestens zwei Stunden im Kühlschrank kühlen, bis es fest ist.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()
        
        # Recipe 2
        category = Category.query.filter_by(name='Dessert').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Castella',
            description='Castella ist ein weicher, luftiger Biskuitkuchen aus Japan mit portugiesischen Wurzeln. Seine feine Honigsüsse macht ihn zum perfekten Teebegleiter und beliebten Mitbringsel, ob pur, mit Matcha oder Schokolade.',
            image='castella.png',
            preparation_time=100,
            portions=5,
            difficulty='Mittel',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Eier', quantity=3,recipe_id=recipe.id),
            Ingredient(name='Zucker', quantity=90, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Honig', quantity=1.5, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Mehl', quantity=90, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Milch', quantity=75, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Speisestärke', quantity=2, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Salz', quantity=1, measurement_unit='Prise', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='Heize den Ofen auf 160 °C Ober-/Unterhitze vor und lege eine rechteckige Form (ca. 20×20 cm) mit Backpapier aus.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Trenne die Eier. Schlage das Eiweiss mit dem Zucker steif. In einer zweiten Schüssel das Eigelb cremig rühren.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Honig und Milch unter das Eigelb rühren. Mehl, Speisestärke und Salz dazusieben und alles zu einem glatten Teig verrühren. Den Eischnee vorsichtig unterheben, damit der Kuchen schön fluffig bleibt.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Den Teig in die Form füllen und die Oberfläche glattstreichen. Eine ofenfeste Schale mit Wasser in den Ofen stellen, denn der Dampf hält den Kuchen saftig und sorgt für ein gleichmässiges Backergebnis. Den Kuchen 50–60 Minuten backen, bis er goldbraun ist und ein Holzstäbchen sauber herauskommt.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Den Kuchen kurz in der Form abkühlen lassen, dann herausnehmen und vollständig auf einem Gitter auskühlen lassen.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()
        
        # Recipe 3
        category = Category.query.filter_by(name='Dessert').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Nyonya Ananas-Törtchen',
            description='Die Nyonya Ananas-Törtchen stammen aus Malakka, Malaysia, und sind ein typisches Gebäck der Peranakan-Küche, die chinesische und malaiische Einflüsse vereint. Ihren Ursprung verdanken sie der portugiesischen Kolonialzeit, als europäische Backtechniken in die Region kamen, darunter das Einreiben von Butter in Mehl für einen zarten, krümeligen Teig. Die reichlich vorhandene Ananas der Region wurde zur charakteristischen Füllung. Bis heute werden die Törtchen traditionell zum chinesischen Neujahr gereicht.',
            image='nyonya_ananas_toertchen.png',
            preparation_time=120,
            portions=6,
            difficulty='Schwierig',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Dose Ananas, abgetropft und klein gehackt ', quantity=1,recipe_id=recipe.id),
            Ingredient(name='Zucker', quantity=30, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Zimtpulver', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Nelkenpulver', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Speisestärke', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Kaltes Wasser', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Mehl', quantity=200, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Eier', quantity=2, recipe_id=recipe.id),
            Ingredient(name='Wasser', quantity=1.5, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Margarine', quantity=100, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Salz', quantity=1, measurement_unit='Prise', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='Die Ananas fein hacken und pürieren. Überschüssigen Saft durch ein Sieb abgiessen, um die Kochzeit der Marmelade zu verkürzen.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Die Ananas zusammen mit Zimt und Nelken in einem Topf bei mittlerer Hitze 25 Minuten köcheln lassen. Dann Zucker hinzufügen und bei niedriger Hitzeweiterkochen, bis die Mischung eine goldbraune Konsistenz erreicht.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Speisestärke im kalten Wasser anrühren, unter die heisse Masse rühren und noch 2–3 Minuten weiterköcheln lassen. Nelken entfernen und die Füllung abkühlen lassen.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Mehl in eine Schüssel geben. Margarine hinzufügen und mit den Fingerspitzen ins Mehl reiben, bis eine krümelige Masse entsteht. ', recipe_id=recipe.id),
            Preparation(step_number=5, description='Ei, Wasser und Salz hinzufügen und kneten.', recipe_id=recipe.id),
            Preparation(step_number=6, description='Den Teig in Frischhaltefolie wickeln und 30 Minuten im Kühlschrank ruhen lassen. ', recipe_id=recipe.id),
            Preparation(step_number=7, description='Den Teig auf einer leicht bemehlten Fläche ausrollen und mit einem Ausstecher kleine Kreise oder Blumen ausstechen. Etwas Ananasfüllung in die Mitte geben. Nach Belieben mit Teig bedecken. Die Oberfläche mit 1 Ei und 1 TL Wasser bestreichen.', recipe_id=recipe.id),
            Preparation(step_number=8, description='Die Törtchen bei 180 °C (Ober-/Unterhitze) 20 Minuten goldgelb backen.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()
        
        # Recipe 4
        category = Category.query.filter_by(name='Dessert').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Bánh Tai Heo ',
            description='Bánh Tai Heo, was übersetzt "Schweineohr-Kekse bedeutet, ist ein beliebter vietnamesischer Snack, der seinen Namen der charakteristischen Spiralform verdankt, die an ein Schweineohr erinnert. Diese knusprigen Kekse sind leicht süss und werden traditionell zu Tee oder Kaffee serviert. Für viele Vietnamesinnen und Vietnamesen wecken sie Kindheitserinnerungen an Strassenstände und Familiennachmittage.',
            image='banh_tai_heo.png',
            preparation_time=180,
            portions=6,
            difficulty='Schwierig',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='ungesalzene Butter', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Puderzucker', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Zitronensaft', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Salz', quantity=1, measurement_unit='Prise', recipe_id=recipe.id),
            Ingredient(name='Eigelb', quantity=2, recipe_id=recipe.id),
            Ingredient(name='Kaltes Wasser', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Kokosmilch', quantity=80, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Weizenmehl', quantity=95, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Weizenmehl', quantity=70, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Kakaopulver', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Pflanzenöl', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='In einer Schüssel Butter, Puderzucker, Zitronensaft und Salz glatt verrühren. Die Eigelbe nacheinander unterrühren, bis die Masse gleichmässig ist. Die Kokosmilch einrühren. Ungefähr die Hälfte des Teigs in eine zweite Schüssel geben.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Zur ersten Schüssel 95 g Mehl geben und rühren. In die zweite Schüssel das restliche Mehl und das Kakaopulver. Jeden Teig in Frischhaltefolie wickeln und 1 Stunde im Kühlschrank kühlen.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Auf einer leicht bemehlten Arbeitsfläche den hellen Teig zu einem groben Rechteck von etwa 0,5 cm Dicke ausrollen.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Den Schokoladenteig genauso ausrollen', recipe_id=recipe.id),
            Preparation(step_number=6, description='Den hellen Teig leicht mit Wasser bestreichen und den Schokoladenteig darauflegen. Drücke sie leicht zusammen, damit sie aneinanderhalten. Dann rolle die beiden Teige von der langen Seite her auf, also wie eine Zimtschneckenrolle. Wickle die Teigrolle in Frischhaltefolie und lege sie 40 Minuten ins Gefrierfach, damit sie fest wird. ', recipe_id=recipe.id),
            Preparation(step_number=7, description='In einer Pfanne etwa 1 cm Öl erhitzen. Während das Öl warm wird, den Teig in Scheiben (ca. 3 mm dick) schneiden. Jede Scheibe mit den Händen flachdrücken. Die Teigscheiben ins heisse Öl geben frittieren, bis sie goldbraun und leicht gewellt sind.', recipe_id=recipe.id),
            Preparation(step_number=8, description='Mit einem Schaumlöffel herausnehmen und auf Küchenpapier abtropfen lassen. Mit dem restlichen Teig genauso weitermachen.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()

        # Recipe 5
        category = Category(name='Hauptgericht')
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Spicy Chicken Curry',
            description='Chicken Curry entstand im 18. Jahrhundert als Mischung aus indischer Gewürzkunst und britischen Zutaten. Britische Kolonialherren brachten Hühnchen nach Indien, und indische Köche kombinierten es geschickt mit ihren typischen Gewürzen und Aromen. Heute wird das aromatische Gericht mit Reis oder Fladenbrot serviert und ist ein fester Bestandteil der indischen Küche.',
            image='spicy_chicken_curry.png',
            preparation_time=40,
            portions=2,
            difficulty='Einfach',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Hähnchenbrust, gewürfelt', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Zwiebel, gehackt', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Knoblauchzehen, fein gehackt', quantity=2, recipe_id=recipe.id),
            Ingredient(name='Ingwer, gerieben', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Kreuzkümmel', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Koriander', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Kurkuma', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Garam Masala', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Curry Pulver', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Chilipulver', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Tomatenpüree', quantity=120, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Kokosmilch', quantity=120, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Salz und Pfeffer nach Geschmack', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='In einer Pfanne etwas Öl erhitzen und die Zwiebeln zusammen mit Knoblauch und Ingwer anbraten, bis sie düften.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Die gewürfelte Hähnchenbrust dazugeben und rundherum goldbraun anbraten.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Die Gewürze Kreuzkümmel, Koriander, Kurkuma, Garam Masala und Chilipulver darüberstreuen und gut unterrühren.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Tomatenpüree und Kokosmilch eingiessen, mit Salz und Pfeffer abschmecken.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Alles 15 bis 20 Minuten sanft köcheln lassen, bis das Hähnchen gar ist und die Sauce eingedickt ist.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()

        # Recipe 6
        category = Category.query.filter_by(name='Hauptgericht').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Thaisuppe',
            description='Thai-Suppen haben ihre Wurzeln in alten Kochtraditionen, bei denen frische Kräuter sowohl für den Geschmack als auch für ihre heilende Wirkung geschätzt wurden. Klassiker wie Tom Yum, eine würzig-saure Suppe, und Tom Kha Gai, eine milde Kokossuppe, zeigen die Vielfalt der thailändischen Küche, die je nach Region und Geschmack viele Varianten kennt. Heute zählen sie zu den bekanntesten Gerichten Thailands und sind weltweit feste Bestandteile der Thai-Küche.',
            image='thaisuppe.png',
            preparation_time=40,
            portions=2,
            difficulty='Einfach',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Kokosöl', quantity=0.5, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Ingwer, fein gehackt', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Knoblauchzehen, fein gehackt', quantity=2, recipe_id=recipe.id),
            Ingredient(name='Frühlingszwiebeln, in feine Ringe geschnitten', quantity=3, recipe_id=recipe.id),
            Ingredient(name='kleine rote Paprika, entkernt und in feine Streifen geschnitten', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Karotten, in dünne diagonale Scheiben geschnitten', quantity=200, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Tomaten, gewürfelt', quantity=150, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='heisses Wasser', quantity=600, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='Kokosmilch', quantity=400, measurement_unit='ml', recipe_id=recipe.id),
            Ingredient(name='abgeriebene Zitronenschale', quantity='1', recipe_id=recipe.id),
            Ingredient(name='Zitronensaft', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Salz', quantity=2, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Chili', quantity=1, measurement_unit='Prise', recipe_id=recipe.id),
            Ingredient(name='Reisnudeln oder Basmatireis', quantity=100, measurement_unit='g', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='Topf mit Wasser aufsetzen und Reis darin kochen.', recipe_id=recipe.id),
            Preparation(step_number=2, description='In einem weiterem Topf Kokosöl erhitzen, Ingwer, Knoblauch und Frühlingszwiebeln kurz anschwitzen.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Paprika, Karotten und Tomaten hinzufügen und unter Rühren anbraten. Mit Kokosmilch und heissem Wasser ablöschen.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Zitronenschale, Zitronensaft und Salz zugeben und 10–15 Minuten leise köcheln lassen. Mit Chili, Salz und eventuell weiterem Zitronensaft abschmecken.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Suppe in Schalen füllen, jeweils einen grossen Löffel gekochten Reis in die Mitte geben.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()

        # Recipe 7
        category = Category.query.filter_by(name='Hauptgericht').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Chow Mein',
            description='Chow Mein ist ein traditionelles chinesisches Nudelgericht, dessen Ursprung bis in die Han-Dynastie zurückreicht. Der Name bedeutet "gebratene Nudeln" und beschreibt die typische Zubereitung im Wok, bei der die Nudeln kurz und heiss angebraten werden. Chow Mein ist in ganz Asien und weit darüber hinaus beliebt und steht für die Wandlungsfähigkeit chinesischer Kochkunst.',
            image='chow_mein.png',
            preparation_time=65,
            portions=2,
            difficulty='Mittel',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()

        ingredients = [
            Ingredient(name='Hähnchenbrust, in dünne Streifen geschnitten', quantity=100, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Spaghetti-Nudeln, gekocht ', quantity=75, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Zwiebel, fein gehackt', quantity=0.5, recipe_id=recipe.id),
            Ingredient(name='Knoblauchzehe, fein gehackt', quantity=0.5, recipe_id=recipe.id),
            Ingredient(name='Paprikaschote, entkernt und längs in dünne Streifen geschnitten', quantity=1,recipe_id=recipe.id),
            Ingredient(name='Karotte, geschält und längs in dünne Streifen geschnitten', quantity=0.5, recipe_id=recipe.id),
            Ingredient(name='Frühlingszwiebel, in dünne Ringe geschnitten', quantity=0.5, recipe_id=recipe.id),
            Ingredient(name='Sojasosse', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Chiliflocken, Pfeffer, Salz nach Geschmack', recipe_id=recipe.id),
            Ingredient(name='Sojasosse', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Zucker', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Speisestärke', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Sonnenblumenöl', quantity=0.5, measurement_unit='EL', recipe_id=recipe.id),
        ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
             Preparation(step_number=1, description='Hähnchenbrust mit Sojasosse, Zucker, Speisestärke und Sonnenblumenöl in einer Schüssel gründlich vermischen. Abdecken und etwa 30 Minuten im Kühlschrank marinieren lassen.', recipe_id=recipe.id),
             Preparation(step_number=2, description='In einer vorgeheizten Pfanne 2 EL Öl erhitzen und die marinierten Hähnchenstreifen scharf anbraten, bis sie rundherum leicht gebräunt sind.', recipe_id=recipe.id),
             Preparation(step_number=3, description='Zwiebel, Knoblauch, Paprika, Karotte und Frühlingszwiebeln in die Pfanne geben und zusammen mit dem Hähnchen erhitzen.', recipe_id=recipe.id),
             Preparation(step_number=4, description='Alles mit 2 EL Sojasosse, Chiliflocken, Pfeffer und bei Bedarf etwas Salz abschmecken.', recipe_id=recipe.id),
             Preparation(step_number=5, description='Die vorgekochten Nudeln in die Pfanne geben und 2–3 Minuten unter Rühren mitbraten, bis sie die Aromen aufgenommen haben.', recipe_id=recipe.id),
        ]
        db.session.add_all(steps)
        db.session.commit()
        
        # Recipe 8
        category = Category.query.filter_by(name='Hauptgericht').first()
        db.session.add(category)
        db.session.commit()

        recipe = Recipe(
            name='Nasi Goreng',
            description='Nasi Goreng gilt als eines der bekanntesten Gerichte Indonesiens und ist eng mit der Alltagsküche des Landes verbunden. Ursprünglich entstand es aus der Idee, übrig gebliebenen Reis weiterzuverwenden, und wurde durch chinesische Einflüsse sowie lokale Gewürze zu einem eigenständigen, aromatischen Gericht. Heute findet man Nasi Goreng in zahlreichen Varianten in ganz Südostasien, von Malaysia über Singapur bis nach Brunei, wobei jede Region ihre eigene Interpretation entwickelt hat.',
            image='nasi_goreng.png',
            preparation_time=30,
            portions=1,
            difficulty='Einfach',
            category_id=category.id
        )
        db.session.add(recipe)
        db.session.commit()
        
        ingredients = [
            Ingredient(name='weisser Reis', quantity=120, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Karotte, geschält und in kleine Würfel geschnitten', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Knoblauchzehe, in feine Scheiben geschnitten', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Zwiebel, in feine Scheiben geschnitten', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Chilipulver', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='süsse Sojasauce', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            Ingredient(name='Hühnerbrühe', quantity=2, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Frühlingszwiebelstiel', quantity=1, recipe_id=recipe.id),
            Ingredient(name='Öl', quantity=2, measurement_unit='EL', recipe_id=recipe.id),
            ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
            Preparation(step_number=1, description='Den Reis in leicht gesalzenem Wasser kochen, bis er gar ist, dann beiseitestellen.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Öl in einer Pfanne erhitzen. Knoblauch und Zwiebeln darin anschwitzen.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Karotten und Chilipulver hinzufügen und unter Rühren kochen, bis die Karotten weich werden.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Gekochten Reis, Hühnerbrühe und süsse Sojasauce in die Pfanne geben und alles gut vermischen.', recipe_id=recipe.id),
            Preparation(step_number=5, description='Zum Schluss die Frühlingszwiebeln unterrühren.', recipe_id=recipe.id),
            ]
        db.session.add_all(steps)
        db.session.commit()

        # Recipe 9
        category = Category.query.filter_by(name='Hauptgericht').first()
        recipe = Recipe(
            name='Pol Roti',
            description='Pol Roti, was übersetzt "Kokosnuss-Fladenbrot" bedeutet, ist eine traditionelle Spezialität aus Sri Lanka, die zu jeder Mahlzeit genossen wird. Ihren Ursprung hat sie in der einfachen Dorfküche, wo aus regionalen Zutaten wie Getreide und Reis frühe Formen von Fladenbrot entstanden. Mit der Verbreitung der Kokospalme entlang der Küsten wurde frisch geriebene Kokosnuss zu einem festen Bestandteil des Teigs und verlieh dem Brot seinen typischen Geschmack. Pol Roti wird oft mit Currys, Chutneys oder dem beliebten Kokos-Sambal serviert.',
            image='pol_roti.png',
            preparation_time=80,
            portions=5,
            difficulty='Einfach',
            category_id=category.id
            )
        db.session.add(recipe)
        db.session.commit()
        
        ingredients = [
            Ingredient(name='Mehl', quantity=250, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Kokosraspeln', quantity=100, measurement_unit='g', recipe_id=recipe.id),
            Ingredient(name='Salz', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='getrocknete Hefe', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Zucker', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
            Ingredient(name='Butter', recipe_id=recipe.id),
            Ingredient(name='Wasser', quantity=150, measurement_unit='ml', recipe_id=recipe.id),
            ]
        db.session.add_all(ingredients)
        db.session.commit()
        
        steps = [
            Preparation(step_number=1, description='In einer Schüssel das Weizenmehl geben und in der Mitte eine kleine Mulde formen. Zucker, Salz, Trockenhefe und Kokosraspeln in die Mulde geben. Wasser hinzufügen. Alles gut miteinander vermischen, bis ein gleichmässiger Teig entsteht. Den Teig etwa 30 Minuten an einem warmen Ort ruhen lassen.', recipe_id=recipe.id),
            Preparation(step_number=2, description='Den Teig in kleine Portionen teilen und zu Kugeln formen. Die Kugeln nochmals 15 Minuten ruhen lassen.', recipe_id=recipe.id),
            Preparation(step_number=3, description='Auf einer leicht bemehlten Arbeitsfläche jede Kugel flach ausrollen, bis etwa 1 cm dicke Fladen entstehen. Eine Pfanne auf mittlerer Hitze erhitzen, etwas Kokosöl oder Butter hineingeben und die Fladen darin von beiden Seiten jeweils 2–3 Minuten goldbraun ausbacken.', recipe_id=recipe.id),
            Preparation(step_number=4, description='Die Pol Roti warm servieren und mit Currys, Chutneys oder Kokos-Sambal geniessen.', recipe_id=recipe.id),
            ]
        db.session.add_all(steps)
        db.session.commit()

        # Recipe 10
        category = Category.query.filter_by(name='Dessert').first()
        recipe = Recipe(
              name='Hotteok',
              description='Ein Hotteok ist ein kleiner Hefepfannkuchen, der traditionell mit Zimt, Rohzucker und Nüssen gefüllt wird. Er wird warm und frisch gegessen und ist als Streetfood ganz besonders im Winter sehr beliebt. Der Hotteok wird in Südkorea meist in einem Pappbecher serviert.',
              image='hotteok.png',
              preparation_time=120,
              portions=5,
              difficulty='Einfach',
              category_id=category.id
              )
        db.session.add(recipe)
        db.session.commit()
        
        ingredients = [
              Ingredient(name='Mehl', quantity=300, measurement_unit='g', recipe_id=recipe.id),
              Ingredient(name='Trockenhefe', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
              Ingredient(name='Zucker', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
              Ingredient(name='Wasser', quantity=170, measurement_unit='ml', recipe_id=recipe.id),
              Ingredient(name='Salz', quantity=0.5, measurement_unit='TL', recipe_id=recipe.id),
              Ingredient(name='Öl', quantity=1, measurement_unit='EL', recipe_id=recipe.id),
              Ingredient(name='brauner Zucker', quantity=30, measurement_unit='g', recipe_id=recipe.id),
              Ingredient(name='Zimt (optional)', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
              Ingredient(name='Wasser', quantity=1, measurement_unit='TL', recipe_id=recipe.id),
              Ingredient(name='Nüsse nach Wahl', quantity=30, measurement_unit='g', recipe_id=recipe.id),
              ]
        db.session.add_all(ingredients)
        db.session.commit()

        steps = [
              Preparation(step_number=1, description='Zuerst das warme Wasser mit dem Zucker und der Trockenhefe verrühren und etwa zehn Minuten stehen lassen, bis die Mischung schäumt. Dann das Mehl in eine Schüssel sieben, Salz und Öl hinzufügen und die Hefemischung darübergiessen. Alles zu einem glatten Teig verkneten und diesen etwa fünf Minuten kräftig durchkneten. Anschliessend die Schüssel abdecken und den Teig eine Stunde an einem warmen Ort ruhen lassen, bis er sein Volumen deutlich vergrössert hat.', recipe_id=recipe.id),
              Preparation(step_number=2, description='Für die Füllung die Nüsse grob hacken und mit dem braunen Zucker, dem Zimt sowie dem Wasser vermengen. Danach den Teig in Stücke teilen und jeweils zu einem kleinen Fladen formen. In die Mitte einen Esslöffel der Nussfüllung geben, die Ränder nach innen einklappen, gut verschliessen und den Teigling anschliessend wieder flachdrücken.', recipe_id=recipe.id),
              Preparation(step_number=3, description='In einer Pfanne etwas Öl erhitzen, die Teiglinge hineingeben und sofort leicht flachdrücken. Bei mittlerer Hitze von beiden Seiten goldbraun braten und warm servieren.', recipe_id=recipe.id),
              ]
        db.session.add_all(steps)
        db.session.commit()

        print("Standardrecipee wurden erfolgreich eingetragen!")
    else:
        print("Datenbank ist bereits befüllt.")
