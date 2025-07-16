def people_object_to_dict(client, people):
  peopledict = dict()
  client = client.strip()
  for person in people:
    fullname = person.name.first + " " + person.name.last + " " + person.name.suffix
    fullname = fullname.strip()
    peopledict[fullname] = fullname
  peopledict[client] = client
  return peopledict