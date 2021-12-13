class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def matches(self, player):
        return True

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return True
        
        return False  

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
            
        return False

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.match_object = matcher

    def build(self):
        return self.match_object

    def playsIn(self, team):
        matcher = PlaysIn(team)
        return QueryBuilder(And(matcher, self.match_object))

    def hasAtLeast(self, value, attr):
        matcher = HasAtLeast(value, attr)
        return QueryBuilder(And(matcher, self.match_object))

    def hasFewerThan(self, value, attr):
        matcher = HasFewerThan(value, attr)
        return QueryBuilder(And(matcher, self.match_object))    