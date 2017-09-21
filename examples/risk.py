from graphscii import Graph

g = Graph()

# North America
g.add_node('Alaska', pos=[0, 0])
g.add_node('Northwest Territory', pos=[0.1, 0.1])
g.add_node('Greenland', pos=[0.3, 0.05])
g.add_node('Alberta', pos=[0.05, 0.2])
g.add_node('Ontario', pos=[0.15, 0.3])
g.add_node('Quebec', pos=[0.25, 0.25])
g.add_node('Western US', pos=[0.05, 0.4])
g.add_node('Eastern US', pos=[0.25, 0.45])
g.add_node('Central America', pos=[0.15, 0.6])
g.add_edge('Alaska', 'Northwest Territory')
g.add_edge('Alaska', 'Alberta')
g.add_edge('Northwest Territory', 'Alberta')
g.add_edge('Northwest Territory', 'Ontario')
g.add_edge('Northwest Territory', 'Greenland')
g.add_edge('Alberta', 'Ontario')
g.add_edge('Alberta', 'Western US')
g.add_edge('Ontario', 'Greenland')
g.add_edge('Ontario', 'Quebec')
g.add_edge('Ontario', 'Western US')
g.add_edge('Ontario', 'Eastern US')
g.add_edge('Greenland', 'Quebec')
g.add_edge('Western US', 'Eastern US')
g.add_edge('Western US', 'Central America')
g.add_edge('Quebec', 'Eastern US')
g.add_edge('Eastern US', 'Central America')

# South America
g.add_node('Venezuela', pos=[0.2, 0.7])
g.add_node('Brazil', pos=[0.3, 0.85])
g.add_node('Peru', pos=[0.15, 0.8])
g.add_node('Argentina', pos=[0.2, 1.0])
g.add_edge('Venezuela', 'Brazil')
g.add_edge('Venezuela', 'Peru')
g.add_edge('Brazil', 'Peru')
g.add_edge('Brazil', 'Argentina')
g.add_edge('Peru', 'Argentina')

# Africa
g.add_node('North Africa', pos=[0.45, 0.65])
g.add_node('Egypt', pos=[0.55, 0.6])
g.add_node('East Africa', pos=[0.65, 0.7])
g.add_node('Congo', pos=[0.5, 0.8])
g.add_node('South Africa', pos=[0.55, 1.0])
g.add_node('Madagascar', pos=[0.6, 0.9])
g.add_edge('North Africa', 'Egypt')
g.add_edge('North Africa', 'East Africa')
g.add_edge('North Africa', 'Congo')
g.add_edge('Egypt', 'East Africa')
g.add_edge('East Africa', 'Congo')
g.add_edge('East Africa', 'Madagascar')
g.add_edge('Congo', 'South Africa')
g.add_edge('Madagascar', 'South Africa')

# Europe
g.add_node('Western Europe', pos=[0.45, 0.5])
g.add_node('Southern Europe', pos=[0.6, 0.45])
g.add_node('Northern Europe', pos=[0.55, 0.35])
g.add_node('Great Britain', pos=[0.4, 0.3])
g.add_node('Iceland', pos=[0.4, 0.2])
g.add_node('Scandinavia', pos=[0.55, 0.1])
g.add_node('Ukraine', pos=[0.65, 0.2])
g.add_edge('Western Europe', 'Southern Europe')
g.add_edge('Western Europe', 'Northern Europe')
g.add_edge('Western Europe', 'Great Britain')
g.add_edge('Southern Europe', 'Northern Europe')
g.add_edge('Southern Europe', 'Ukraine')
g.add_edge('Northern Europe', 'Great Britain')
g.add_edge('Northern Europe', 'Ukraine')
g.add_edge('Northern Europe', 'Scandinavia')
g.add_edge('Great Britain', 'Scandinavia')
g.add_edge('Great Britain', 'Iceland')
g.add_edge('Ukraine', 'Scandinavia')
g.add_edge('Scandinavia', 'Iceland')

# Asia
g.add_node('Middle East', pos=[0.7, 0.55])
g.add_node('Afghanistan', pos=[0.75, 0.4])
g.add_node('India', pos=[0.8, 0.6])
g.add_node('Ural', pos=[0.75, 0.15])
g.add_node('China', pos=[0.85, 0.5])
g.add_node('Siberia', pos=[0.825, 0.2])
g.add_node('Mongolia', pos=[0.95, 0.4])
g.add_node('Yakutsk', pos=[0.9, 0.1])
g.add_node('Irkutsk', pos=[0.9, 0.25])
g.add_node('Kamchatka', pos=[1.0, 0.0])
g.add_node('Japan', pos=[1.0, 0.25])
g.add_node('Siam', pos=[0.9, 0.65])
g.add_edge('Middle East', 'Afghanistan')
g.add_edge('Middle East', 'India')
g.add_edge('Afghanistan', 'India')
g.add_edge('Afghanistan', 'Ural')
g.add_edge('Afghanistan', 'China')
g.add_edge('India', 'China')
g.add_edge('India', 'Siam')
g.add_edge('Ural', 'China')
g.add_edge('Ural', 'Siberia')
g.add_edge('China', 'Siam')
g.add_edge('China', 'Siberia')
g.add_edge('China', 'Mongolia')
g.add_edge('Siberia', 'Mongolia')
g.add_edge('Siberia', 'Yakutsk')
g.add_edge('Siberia', 'Irkutsk')
g.add_edge('Mongolia', 'Irkutsk')
g.add_edge('Mongolia', 'Kamchatka')
g.add_edge('Mongolia', 'Japan')
g.add_edge('Yakutsk', 'Irkutsk')
g.add_edge('Yakutsk', 'Kamchatka')
g.add_edge('Irkutsk', 'Kamchatka')
g.add_edge('Kamchatka', 'Japan')

# Australia
g.add_node('Indonesia', pos=[0.95, 0.7])
g.add_node('New Guinea', pos=[1.0, 0.8])
g.add_node('Western Australia', pos=[0.9, 0.9])
g.add_node('Eastern Australia', pos=[1.0, 1.0])
g.add_edge('Indonesia', 'New Guinea')
g.add_edge('Indonesia', 'Western Australia')
g.add_edge('New Guinea', 'Western Australia')
g.add_edge('New Guinea', 'Eastern Australia')
g.add_edge('Western Australia', 'Eastern Australia')

# Connections
g.add_edge('Siam', 'Indonesia', label='+')
g.add_edge('Southern Europe', 'Middle East', label='+')
g.add_edge('Ukraine', 'Ural', label='+')
g.add_edge('Ukraine', 'Afghanistan', label='+')
g.add_edge('Ukraine', 'Middle East', label='+')
g.add_edge('North Africa', 'Western Europe', label='+')
g.add_edge('North Africa', 'Southern Europe', label='+')
g.add_edge('Egypt', 'Middle East', label='+')
g.add_edge('Egypt', 'Southern Europe', label='+')
g.add_edge('East Africa', 'Middle East', label='+')
g.add_edge('Brazil', 'North Africa', label='+')
g.add_edge('Alaska', 'Kamchatka', label='+')
g.add_edge('Greenland', 'Iceland', label='+')
g.add_edge('Central America', 'Venezuela', label='+')

g.draw()