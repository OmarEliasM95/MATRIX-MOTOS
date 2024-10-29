const labelOption = {
    show: false,
};

const getOptionChart1 = () => {
    return {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Compras', 'Ventas', 'Gastos', 'Ingresos','Egresos']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            right:'left',
            top: 'center',
            feature: {
                mark: { show: true },
                dataView: { show: false, readOnly: false },
                magicType: { show: true, type: ['line', 'bar', 'stack'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: { show: true },
                data: valuesPeriodo
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: 'Compras', 
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [compras]
            },
            {
                name: 'Ventas',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [ventas]
            },
            {
                name: 'Gastos',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [gastos]
            },
            {
                name: 'Ingresos',
                type: 'bar',
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [ingresos]
            },
            {
                name: 'Egresos', 
                type: 'bar',
                barGap: 0,
                label: labelOption,
                emphasis: {
                    focus: 'series'
                },
                data: [egresos]
            },
        ]
    };
};

const initCharts = () => {
    const chart1 = echarts.init(document.getElementById('chart1'));
    chart1.setOption(getOptionChart1());
};

window.addEventListener("load", () => {
    initCharts();
});
