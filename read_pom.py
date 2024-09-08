import xml.etree.ElementTree as ET

tree = ET.parse('/home/sdn/Desktop/project4_311581030/pom.xml')
root = tree.getroot()

namespace = {'mvn': 'http://maven.apache.org/POM/4.0.0'}

group_id = root.find('mvn:groupId', namespace).text
artifact_id = root.find('mvn:artifactId', namespace).text
version = root.find('mvn:version', namespace).text

onos_app_name = root.find('mvn:properties/mvn:onos.app.name', namespace).text

print("GroupId: {}".format(group_id))
print("ArtifactId: {}".format(artifact_id))
print("Version: {}".format(version))
print("ONOS App Name: {}".format(onos_app_name))
