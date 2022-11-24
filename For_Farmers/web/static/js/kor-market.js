(async () => {

    const topology = await fetch(
      'https://code.highcharts.com/mapdata/countries/kr/kr-all.topo.json'
    ).then(response => response.json());
  
    // Initialize the chart
    Highcharts.mapChart('container', {
  
      chart: {
        map: topology
      },
  
      title: {
        text: '가까운 농산물 도매시장 위치를 확인해보세요!'
      },
      subtitle:{
        text: '출처: 도매시장 통합홈페이지'
      },
      accessibility: {
        description: 'Map where city locations have been defined using latitude/longitude.'
      },
  
      mapNavigation: {
        enabled: true
      },
  
      tooltip: {
        headerFormat: '',
        pointFormat: '<b>{point.name}</b><br>{point.market}'
      },
  
      series: [{
        // Use the gb-all map with no data as a basemap
        name: 'South Korea',
        borderColor: '#A0A0A0',
        nullColor: 'rgba(200, 200, 200, 0.3)',
        showInLegend: false
      }, {
        name: 'Separators',
        type: 'mapline',
        nullColor: '#707070',
        showInLegend: false,
        enableMouseTracking: false,
        accessibility: {
          enabled: false
        }
      }, {
        // Specify points using lat/lon
        type: 'mappoint',
        name: '농산물도매시장',
        accessibility: {
          point: {
            valueDescriptionFormat: '{xDescription}. Lat: {point.lat:.2f}, lon: {point.lon:.2f}, market: {point.market:2f}.'
          }
        },
        color: Highcharts.getOptions().colors[1],
        data: [{
          name: '부산',
          lat: 35.1796,
          lon: 129.0756,
          market: '부산반여농산물도매시장(051-550-8211), 부산엄궁농산물도매시장(051-310-8282)'
        }, {
          name: '서울',
          lat: 37.5665,
          lon: 126.9780,
          market: '서울가락농수산물도매시장(02-3435-1000), 서울강서농산물도매시장(02-2640-6000)'
        }, {
          name: '대구',
          lat: 35.8714,
          lon: 128.6014,
          market: '대구북부농수산물도매시장(053-803-7000)'
        }, {
          name: '인천',
          lat: 37.4563,
          lon: 126.7052,
          market: '인천남촌농산물도매시장(032-426-8303), 인천삼산농산물도매시장(032-440-6450)'
        }, {
          name: '광주',
          lat: 35.1595,
          lon: 126.8526,
          market: '광주각화농산물도매시장(062-613-5522), 광주서부농수산물도매시장(062-613-5475)'
        }, {
          name: '대전',
          lat: 36.3504,
          lon: 127.3845,
          market: '대전오정농수산물도매시장(042-622-3387), 대전노은농산물도매시장(042-270-7944)'
        }, {
          name: '수원',
          lat: 37.2636,
          lon: 127.0286,
          market: '수원농수산물도매시장(031-228-2723)'
        }, {
          name: '구리',
          lat: 37.5943,
          lon: 127.1296,
          market: '구리농수산물도매시장(031-560-5100)'
        }, {
          name: '울산',
          lat: 35.5384,
          lon: 129.3114,
          market: '울산농수산물도매시장(052-267-7220)'
        }, {
          name: '춘천',
          lat: 37.8813,
          lon: 127.7300,
          market: '춘천농산물도매시장(033-253-3891)'
        }, {
          name: '원주',
          lat: 37.3422,
          lon: 127.9202,
          market: '원주농산물도매시장(033-737-4350)'
        }, {
          name: '강릉',
          lat: 37.7519,
          lon: 128.8761,
          market: '강릉농산물도매시장(033-646-4654)'
        }, {
          name: '청주',
          lat: 36.6424,
          lon: 127.4890,
          market: '청주농수산물도매시장(043-201-2251)'
        }, {
          name: '천안',
          lat: 36.8151,
          lon: 127.1139,
          market: '천안농산물도매시장(041-521-2842)'
        },  {
          name: '전주',
          lat: 35.8242,
          lon: 127.1480,
          market: '전주농수산물도매시장(063-281-5372)'
        },  {
          name: '익산',
          lat: 35.9483,
          lon: 126.9576,
          market: '익산농수산물도매시장(063-843-7747)'
        }, {
          name: '정읍',
          lat: 35.5699,
          lon: 126.8559,
          market: '정읍농산물도매시장(063-532-4001)'
        }, {
          name: '순천',
          lat: 34.9506,
          lon: 127.4872,
          market: '순천농산물도매시장(061-749-8811)'
        }, {
          name: '포항',
          lat: 36.0190,
          lon: 129.3435,
          market: '포항농산물도매시장(054-270-4787)'
        }, {
          name: '안동',
          lat: 36.5684,
          lon: 128.7294,
          market: '안동농산물도매시장(054-859-4070)'
        }, {
          name: '구미',
          lat: 36.1195,
          lon: 128.3446,
          market: '구미농산물도매시장(054-480-4751)'
        }, {
          name: '창원',
          lat: 35.2538,
          lon: 128.6403,
          market: '창원팔용농산물도매시장(055-225-7861), 창원내서농산물도매시장(055-225-7821)'
        }, {
          name: '진주',
          lat: 35.1800,
          lon: 128.1076,
          market: '진주농산물도매시장(055-749-6195)'
        }]
      }]
    });
  
  })();
  