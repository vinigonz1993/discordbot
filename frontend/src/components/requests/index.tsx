import axios from 'axios';

export default {
    oct: {
        get: () => axios.get(
            'https://vinigonz1993.pythonanywhere.com//oct',
            {
                method: 'GET',
                params: {
                    stopNo: 1222,
                    routeNo: 57
                },
            },
        ),
    },
};