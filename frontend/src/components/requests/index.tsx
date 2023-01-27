import axios from 'axios';

export default {
    oct: {
        get: () => axios.get(
            'https://127.0.0.1:5000/oct',
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