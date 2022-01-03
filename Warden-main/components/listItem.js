import React from 'react';
import type {Node} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
} from 'react-native';

const ListContent = ({title, location, time}): Node => {

  const isDarkMode = useColorScheme() === 'dark';

  return (
    
    <View style={[styles.sectionContainer, {flexDirection: "column"}]}>
       <Text>{title}</Text>
       <Text>{location}</Text>
       <Text>{time}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
    height: 100,
  },

  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },

  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },

  highlight: {
    fontWeight: '700',
  },
});

export default ListContent;