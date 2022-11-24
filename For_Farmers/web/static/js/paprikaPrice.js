Highcharts.chart('container1', {
    chart: {
    type: 'column',
    options3d: {
        enabled: true,
        alpha: 10,
        beta: 25,
        depth: 70
        }
    },
    title: {
        text: '파프리카 상품 도매가격, 2021 (5kg 단위)'
    },
    subtitle: {
        text: '출처: KAMIS 농산물 유통정보' },
    plotOptions: {
        column: {
            depth: 25
        }
    },
    xAxis: {
        categories: ['1월', '2월', '3월', '4월', '5월', '6월', '7월',
            '8월', '9월', '10월', '11월', '12월'],
        labels: {
            skew3d: true,
            style: {
                fontSize: '16px'
            }
        }
    },
    yAxis: {
        title: {
            text: '원(KRW)',
            margin: 20
        }
    },
    tooltip: {
        valueSuffix: ' 원'
    },
    series: [{
        name: '월별 평균 도매가',
        data: [36987, 36158, 35530, 26824, 22591,
            20155, 19859, 23988, 31684, 26308, 19055, 23305]
    }]
});