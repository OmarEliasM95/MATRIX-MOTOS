const getOptionChart1 = () => {
    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Efectivo', 'Transferencia', 'T. Débito'] 
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            right: 'left',
            top: 'center',
            feature: {
                mark: { show: true },
                dataView: { show: false, readOnly: false },
                magicType: { show: false, type: ['line', 'bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: { show: true },
                data: periodo
            }
        ],
        yAxis: [
            {
                type: 'value',
            }
        ],
        series: [
            {
                name: 'Efectivo', 
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [total_efectivo_compra]  
            },
            {
                name: 'Transferencia',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [total_transferencia_compra]  
            },
            {
                name: 'T. Débito',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [total_tarjeta_debito_compra]  
            },
        ]
    };
};

const initCharts = () => {
    const chart1 = echarts.init(document.getElementById('chart2'));
    chart1.setOption(getOptionChart1());
};

window.addEventListener("load", () => {
    initCharts();
});
