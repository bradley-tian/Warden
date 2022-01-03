import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const Card = ({title, location, time}): Node => {
  return (
    <View style={styles.card}>
      <View style={styles.cardContent}>
        <Text style={styles.titleText}>{title}</Text>
        <Text>{location}</Text>
        <Text>{time}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderRadius: 6,
    elevation: 3,
    backgroundColor: '##ff6363',
    shadowOffset: { width: 1, height: 1 },
    shadowColor: '#333',
    shadowOpacity: 0.3,
    shadowRadius: 2,
    marginHorizontal: 4,
    marginVertical: 12,
  },
  cardContent: {
    marginHorizontal: 18,
    marginVertical: 20,
  },
  titleText: {
    fontWeight: "700",
    fontSize: 20,
  }
});

export default Card;